using MongoDB.Driver;
using MongoDB.Bson;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Connection to mongodb\n");
        string connection_string = "mongodb://localhost:27017/";
        var client = new MongoClient(connection_string);
        var collection = client.GetDatabase("T2308M").GetCollection<BsonDocument>("users");
        // foreach (BsonDocument doc in collection.Aggregate<BsonDocument>().ToList())
        // {
        //     System.Console.WriteLine(string.Format("{0} - {1}", "User Name: ", doc["username"]));
        //     System.Console.WriteLine(string.Format("{0} - {1}\n", "User Name: ", doc["fullname"]));
        // }

        var firstDocument = collection.Find(new BsonDocument()).FirstOrDefault();

        if (firstDocument == null)
        {
            System.Console.WriteLine("Error when connect to db");
        } else {
            foreach (BsonDocument doc in collection.Aggregate<BsonDocument>().ToList())
        {
            System.Console.WriteLine(string.Format("{0} - {1}", "User Name: ", doc["username"]));
            System.Console.WriteLine(string.Format("{0} - {1}\n", "User Name: ", doc["fullname"]));
        }
        }
    }
}